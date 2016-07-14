Name:     ocaml-bytes

Version:  1.4
Release:  1
Summary:  OCAML bytes module
License:  GPLv2+
URL:      https://github.com/chambart/ocaml-bytes
Source0:  https://github.com/chambart/ocaml-bytes/archive/ocaml-bytes.1.4.tar.gz

BuildRequires: ocaml

%prep
%setup -q -n ocaml-bytes-ocaml-bytes.1.4
./configure --libdir=/

%build
make

%install
DESTDIR=%{buildroot}/usr/lib64/ocaml
mkdir -p %{buildroot}/usr/lib64/ocaml
make DESTDIR=%{buildroot}/usr/lib64/ocaml install

%files
/usr/lib64/ocaml/bytes/META
/usr/lib64/ocaml/bytes/bytes.a
/usr/lib64/ocaml/bytes/bytes.cma
/usr/lib64/ocaml/bytes/bytes.cmi
/usr/lib64/ocaml/bytes/bytes.cmo
/usr/lib64/ocaml/bytes/bytes.cmx
/usr/lib64/ocaml/bytes/bytes.cmxa
/usr/lib64/ocaml/bytes/bytes.cmxs

%description
Bytes module for ocaml <= 4.02

%changelog
* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version

