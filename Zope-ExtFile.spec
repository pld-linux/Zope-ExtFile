%define		zope_subname	ExtFile
Summary:	Product stores large files in an external file-repository
Summary(pl.UTF-8):   Produkt umożliwiający obsługę dużych plików w zewnętrznych repozytoriach
Name:		Zope-%{zope_subname}
Version:	1.4.4
Release:	1
License:	Distributable
Group:		Development/Tools
Source0:	http://zope.org/Members/shh/%{zope_subname}/%{version}/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	4e13441da832a904cb75ad367388ae8b
URL:		http://zope.org/Members/shh/ExtFile/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
%pyrequires_eq	python-modules
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope
Requires:	python-Imaging
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ExtFile Product stores large files in an external file-repository
and is able to display icons for different MIME-Types.

%description -l pl.UTF-8
Produkt ExtFile umożliwia obsługę dużych plików w zewnętrznych
repozytoriach i wyświetlanie ich ikonek dla różnych typów MIME.

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
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc doc-1.1/ CHANGES.txt README.txt UPGRADE.txt
%{_datadir}/%{name}
