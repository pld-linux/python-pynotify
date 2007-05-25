Summary:	Python bindings for libnotify
Summary(pl.UTF-8):	Wiązania Pythona do libnotify
Name:		python-pynotify
Version:	0.1.1
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://galago-project.org/files/releases/source/notify-python/notify-python-%{version}.tar.gz
# Source0-md5:	8f0ef0939cc8edd2efd896ce5ba80cf4
BuildRequires:	libnotify-devel >= 0.4.3
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-pygtk-devel >= 2:2.4.0
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
Requires:	libnotify >= 0.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for libnotify.

%description -l pl.UTF-8
Wiązania Pythona do libnotify.

%prep
%setup -q -n notify-python-%{version}

%build
%configure
%{__make} \
	PYTHON="%{__python}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PYTHON="%{__python}" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{py_sitedir}/gtk-2.0/pynotify
%{py_sitedir}/gtk-2.0/pynotify/*.py*
%attr(755,root,root) %{py_sitedir}/gtk-2.0/pynotify/*.so
