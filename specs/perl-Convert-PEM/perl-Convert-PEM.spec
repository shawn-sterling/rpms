# $Id$
# Authority: dries
# Upstream: Benjamin Trott <cpan$stupidfool,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Convert-PEM

Summary: Read/write encrypted ASN.1 PEM files
Name: perl-Convert-PEM
Version: 0.07
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-PEM/

Source: http://search.cpan.org/CPAN/authors/id/B/BT/BTROTT/Convert-PEM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Convert::ASN1)
BuildRequires: perl(Class::ErrorHandler), perl(Crypt::DES_EDE3)

%description
This is Convert::PEM, a module implementing read/write access
to ASN.1-encoded PEM files (with optional encryption).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Convert/PEM.pm
%{perl_vendorlib}/Convert/PEM

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Updated to release 0.07.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
