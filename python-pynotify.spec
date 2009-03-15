Summary:	Python bindings for libnotify
Summary(pl.UTF-8):	Wiązania Pythona do libnotify
Name:		python-pynotify
Version:	0.1.1
Release:	4
License:	LGPL v2.1
Group:		Libraries/Python
Source0:	http://galago-project.org/files/releases/source/notify-python/notify-python-%{version}.tar.gz
# Source0-md5:	8f0ef0939cc8edd2efd896ce5ba80cf4
Patch0:		python-pynotify-codegen.patch
URL:		http://galago-project.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libnotify-devel >= 0.4.3
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-pygtk-devel >= 2:2.4.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
Requires:	libnotify >= 0.4.3
Requires:	python-pygtk-gtk >= 2:2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for libnotify.

%description -l pl.UTF-8
Wiązania Pythona do libnotify.

%package devel
Summary:	Development files for libnotify Python bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Pythona do libnotify
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygtk-devel >= 2:2.4.0

%description devel
Development files for libnotify Python bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Pythona do libnotify.

%prep
%setup -q -n notify-python-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make} clean
%{__make} \
	PYTHON="%{__python}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PYTHON="%{__python}" \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/pynotify/*.la
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%dir %{py_sitedir}/gtk-2.0/pynotify
%{py_sitedir}/gtk-2.0/pynotify/__init__.py[co]
%attr(755,root,root) %{py_sitedir}/gtk-2.0/pynotify/_pynotify.so

%files devel
%defattr(644,root,root,755)
%{_datadir}/pygtk/2.0/defs/pynotify.defs
%{_pkgconfigdir}/notify-python.pc
