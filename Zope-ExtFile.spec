%include	/usr/lib/rpm/macros.python
%define		zope_subname	ExtFile
Summary:	Product stores large files in an external file-repository
Summary(pl):	Produkt umo�liwiaj�cy obs�uge du�ych plik�w w zewn�trznych repozytoriach
Name:		Zope-%{zope_subname}
Version:	1.2.0
Release:	1
License:	Distributable
Group:		Development/Tools
Source0:	http://zope.org/Members/shh/%{zope_subname}/%{version}/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	8aeec9b5893dd194fa08efbbd4d346ac
URL:		http://zope.org/Members/shh/ExtFile/
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
Produkt ExtFile umo�liwia obs�ug� du�ych plik�w w zewn�trznych
repozytoriach i wy�wietlanie ich ikonek dla r�nych typ�w MIME.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,dtml,icons,tests,www,*.py,version.txt,refresh.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

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
%doc CHANGES*.txt LICENSE.txt README.txt UPGRADE*.txt
%{_datadir}/%{name}
