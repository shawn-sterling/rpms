# $Id$
# Authority: dries
# Upstream: Christoph Appel <cappel$web,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-ECB

Summary: Encrypt Data using ECB Mode
Name: perl-Crypt-ECB
Version: 1.40
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-ECB/

Source: http://search.cpan.org/CPAN/authors/id/A/AP/APPEL/Crypt-ECB-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module is a Perl-only implementation of the ECB mode. In
combination with a block cipher such as DES, IDEA or Blowfish, you can
encrypt and decrypt messages of arbitrarily long length. Though for
security reasons other modes than ECB such as CBC should be preferred.
See textbooks on cryptography if you want to know why.

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
%doc CHANGES README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Crypt/ECB.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.40-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.40-1
- Initial package.
