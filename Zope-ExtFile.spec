%include	/usr/lib/rpm/macros.python
%define		zope_subname	ExtFile
Summary:	Product stores large files in an external file-repository
Summary(pl):	Produkt umo¿liwiaj±cy obs³uge du¿ych plików w zewnêtrznych repozytoriach
Name:		Zope-%{zope_subname}
Version:	1.1.3
Release:	1
License:	Distributable
Group:		Development/Tools
Source0:	http://zope.org/Members/MacGregor/%{zope_subname}/%{version}/%{zope_subname}-%{version}.tgz
# Source0-md5:	c5963b22b83a9ee0bb3fe46e525f38c0
URL:		http://zope.org/Members/MacGregor/ExtFile/
%pyrequires_eq	python-modules
Requires:	ImageMagick
Requires:	Zope
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ExtFile Product stores large files in an external file-repository
and is able to display icons for different MIME-Types.

%description -l pl
Produkt ExtFile umo¿liwia obs³ugê du¿ych plików w zewnêtrznych
repozytoriach i wy¶wietlanie ich ikonek dla ró¿nych typów MIME.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {icons,www,*.py,*.dtml,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
        /usr/sbin/installzopeproduct -d %{zope_subname}
        if [ -f /var/lock/subsys/zope ]; then
                /etc/rc.d/init.d/zope restart >&2
        fi
fi

%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.txt
%{_datadir}/%{name}
