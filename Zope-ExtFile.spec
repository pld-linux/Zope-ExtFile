%define		zope_subname	ExtFile
Summary:	Product stores large files in an external file-repository
Summary(pl):	Produkt umo¿liwiaj±cy obs³ugê du¿ych plików w zewnêtrznych repozytoriach
Name:		Zope-%{zope_subname}
Version:	1.4.4
Release:	1
License:	Distributable
Group:		Development/Tools
Source0:	http://zope.org/Members/shh/%{zope_subname}/%{version}/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	4e13441da832a904cb75ad367388ae8b
URL:		http://zope.org/Members/shh/ExtFile/
BuildRequires:	python
%pyrequires_eq	python-modules
Requires:	python-Imaging
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

cp -af {Extensions,dtml,icons,tests,utilities,www,*.py,version.txt,refresh.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

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
%doc doc-1.1/ CHANGES.txt README.txt UPGRADE.txt
%{_datadir}/%{name}
