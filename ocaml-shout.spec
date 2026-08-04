Name:		ocaml-shout
Version:	0.2.7
Release:	6
Summary:	OCaml bindings for the shout library
License:	GPLv2+
Group:		Development/OCaml
URL:		https://sourceforge.net/projects/savonet/files/
Source0:	http://downloads.sourceforge.net/savonet/ocaml-shout/ocaml-shout-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	ocaml
BuildRequires:	ocaml-compiler
BuildRequires:	ocaml-findlib
BuildRequires:	pkgconfig(shout)

%description
This OCaml library interfaces the shout C library which can be used for
communicating with and sending data to Icecast and Icecast 2 streaming
audio servers (they currently support Ogg Vorbis and MP3 audio streams).
It handles the socket connection, the timing of the data transmission,
and prevents bad data from getting to the server.

%package	devel
Summary:	Development files for %{name}
Group:		Development/OCaml
Requires:	%{name} = %{EVRD}

%description	devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
# Old OCamlMakefile + LTO / --no-undefined breaks configure and ocamlmklib
export CC=%{__cc}
export CFLAGS="$(echo "%{optflags}" | sed 's/-flto//g') -fPIC"
export LDFLAGS=
./configure --libdir=%{_libdir} CC=%{__cc} CFLAGS="$CFLAGS"
make all opt CFLAGS="$CFLAGS" LDFLAGS=
make doc || :

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
