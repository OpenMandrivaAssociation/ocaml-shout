Name:           ocaml-shout
Version:        0.2.7
Release:        2
Summary:        OCaml bindings for the shout library
License:        GPL
Group:          Development/Other
URL:            http://sourceforge.net/projects/savonet/files/
Source0:        http://downloads.sourceforge.net/savonet/ocaml-shout/ocaml-shout-%{version}.tar.gz
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml
BuildRequires:  libshout-devel

%description
This OCaml library interfaces the shout C library which can be used for
communicating with and sending data to Icecast and Icecast 2 streaming
audio servers (they currently support Ogg Vorbis and MP3 audio streams).
It handles the socket connection, the timing of the data transmission,
and prevents bad data from getting to the server.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
./configure
make all opt
make doc

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/shout
make install

%files
%defattr(-,root,root)
%doc COPYING README CHANGES
%dir %{_libdir}/ocaml/shout
%{_libdir}/ocaml/shout/META
%{_libdir}/ocaml/shout/*.cma
%{_libdir}/ocaml/shout/*.cmi
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%doc doc/html
%doc examples
%{_libdir}/ocaml/shout/*.a
%{_libdir}/ocaml/shout/*.cmxa
%{_libdir}/ocaml/shout/*.cmx
%{_libdir}/ocaml/shout/*.mli



%changelog
* Mon Jan 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.7-1mdv2010.1
+ Revision: 496351
- update to new version 0.2.7

* Fri Sep 04 2009 Florent Monnier <blue_prawn@mandriva.org> 0.2.6-1mdv2010.0
+ Revision: 430807
- import ocaml-shout

