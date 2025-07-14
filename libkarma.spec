Summary:	Rio Karma access library
Name:		libkarma
Version:	0.1.2
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://www.freakysoft.de/libkarma/%{name}-%{version}.tar.gz
# Source0-md5:	2fe636b011dca1cd2a78cd189b891ed8
Patch0:		%{name}-makefile.patch
URL:		http://www.freakysoft.de/libkarma/
BuildRequires:	mono-csharp
BuildRequires:	taglib-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libkarma is a C language library that provides (read/write) access to
the Rio Karma music player using either the usb (with OMFS) or network
(PEARL) interface.

%package devel
Summary:	Header files for libkarma library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libkarma
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libkarma library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libkarma.

%package static
Summary:	Static libkarma library
Summary(pl.UTF-8):	Statyczna biblioteka libkarma
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libkarma library.

%description static -l pl.UTF-8
Statyczna biblioteka libkarma.

%package -n dotnet-karma-sharp
Summary:	.NET language bindings for libkarma
Summary(pl.UTF-8):	Wiązania .NET do biblioteki libkarma
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n dotnet-karma-sharp
This package provides bindings for .NET to libkarma library.

%description -n dotnet-karma-sharp -l pl.UTF-8
Ten pakiet dostarcza wiązania dla .NET do biblioteki libkarma.

%package -n dotnet-karma-sharp-devel
Summary:	karma# development files
Summary(pl.UTF-8):	Pliki programistyczne karma#
Group:		Development/Libraries
Requires:	dotnet-karma-sharp = %{version}-%{release}

%description -n dotnet-karma-sharp-devel
karma# development files.

%description -n dotnet-karma-sharp-devel -l pl.UTF-8
Pliki programistyczne karma#.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} -j1 \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libkarma

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog THANKS TODO
%attr(755,root,root) %{_bindir}/chprop
%attr(755,root,root) %{_bindir}/karma_helper
%attr(755,root,root) %{_bindir}/riocp
%attr(755,root,root) %{_libdir}/libkarma.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkarma.so.0
%{_mandir}/man1/chprop.1*
%{_mandir}/man1/karma_helper.1*
%{_mandir}/man1/riocp.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkarma.so
%{_includedir}/libkarma

%files static
%defattr(644,root,root,755)
%{_libdir}/libkarma.a

%files -n dotnet-karma-sharp
%defattr(644,root,root,755)
%{_prefix}/lib/karma-sharp

%files -n dotnet-karma-sharp-devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/karma-sharp.pc
