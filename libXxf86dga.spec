Summary: X.Org X11 libXxf86dga runtime library
Name: libXxf86dga
Version: 1.1.1
Release: 1%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0: ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2

BuildRequires: pkgconfig
BuildRequires: xorg-x11-proto-devel >= 7.4-32
BuildRequires: libX11-devel
BuildRequires: libXext-devel

%description
X.Org X11 libXxf86dga runtime library

%package devel
Summary: X.Org X11 libXxf86dga development package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXxf86dga development package

%prep
%setup -q

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
# FIXME: Some of these files are missing %doc AUTHORS COPYING README INSTALL ChangeLog
%doc COPYING ChangeLog
%{_libdir}/libXxf86dga.so.1
%{_libdir}/libXxf86dga.so.1.0.0

%files devel
%defattr(-,root,root,-)
%{_libdir}/libXxf86dga.so
%{_libdir}/pkgconfig/xxf86dga.pc
%{_mandir}/man3/*.3*
%{_includedir}/X11/extensions/Xxf86dga.h
%{_includedir}/X11/extensions/xf86dga1.h

%changelog
* Mon Oct 26 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.1.1-1
- libXxf86dga 1.1.1
  Requires xorg-x11-proto-devel for new xf86dgaproto.

* Fri Aug 28 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.0.99.1-1
- libXxf86dga 1.0.99.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Adam Jackson <ajax@redhat.com> 1.0.2-5
- Un-require xorg-x11-filesystem

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Adam Jackson <ajax@redhat.com> 1.0.2-3
- Fix license tag.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.2-2
- Autorebuild for GCC 4.3

* Mon Dec 03 2007 Adam Jackson <ajax@redhat.com> 1.0.2-1
- libXxf86dga 1.0.2

* Tue Aug 21 2007 Adam Jackson <ajax@redhat.com> - 1.0.1-4
- Rebuild for build id

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Fri Jun 09 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-3
- Added "Requires: xorg-x11-proto-devel" to devel package for xxf86dga.pc

* Mon Jun 05 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-2
- Added "BuildRequires: pkgconfig" for (#193507)
- Replace "makeinstall" with "make install DESTDIR=..." for (#192728)

* Thu Apr 27 2006 Adam Jackson <ajackson@redhat.com> 1.0.1-1
- Update to 1.0.1

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.0-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.0-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 23 2006 Mike A. Harris <mharris@redhat.com> 1.0.0-2
- Bumped and rebuilt

* Fri Dec 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Updated libXxf86dga to version 1.0.0 from X11R7 RC4

* Tue Dec 13 2005 Mike A. Harris <mharris@redhat.com> 0.99.3-1
- Updated libXxf86dga to version 0.99.3 from X11R7 RC3
- Added "Requires(pre): xorg-x11-filesystem >= 0.99.2-3", to ensure
  that /usr/lib/X11 and /usr/include/X11 pre-exist.
- Removed 'x' suffix from manpage directories to match RC3 upstream.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 11 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-1
- Updated libXxf86dga to version 0.99.2 from X11R7 RC2
- Changed 'Conflicts: XFree86-devel, xorg-x11-devel' to 'Obsoletes'
- Changed 'Conflicts: XFree86-libs, xorg-x11-libs' to 'Obsoletes'


* Mon Oct 24 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-1
- Updated libXxf86dga to version 0.99.1 from X11R7 RC1
- Updated file manifest to find manpages in "man3x"

* Thu Sep 29 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-3
- Renamed package to remove xorg-x11 from the name due to unanimous decision
  between developers.
- Use Fedora Extras style BuildRoot tag.
- Disable static library creation by default.
- Add missing defattr to devel subpackage
- Add missing documentation files to doc macro

* Tue Aug 23 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-2
- Renamed package to prepend "xorg-x11" to the name for consistency with
  the rest of the X11R7 packages.
- Added "Requires: %%{name} = %%{version}-%%{release}" dependency to devel
  subpackage to ensure the devel package matches the installed shared libs.
- Added virtual "Provides: lib<name>" and "Provides: lib<name>-devel" to
  allow applications to use implementation agnostic dependencies.
- Added post/postun scripts which call ldconfig.
- Added Conflicts with XFree86-libs and xorg-x11-libs to runtime package,
  and Conflicts with XFree86-devel and xorg-x11-devel to devel package.

* Mon Aug 22 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-1
- Initial build.
