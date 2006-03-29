# $Id$
# Authority: dries
# Upstream: Sean M. Burke <sburke$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tree-DAG_Node

Summary: (super)class for representing nodes in a tree
Name: perl-Tree-DAG_Node
Version: 1.05
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tree-DAG_Node/

Source: http://search.cpan.org/CPAN/authors/id/S/SB/SBURKE/Tree-DAG_Node-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Tree::DAG_Node is a (super)class for representing nodes in a tree.

This class encapsulates/makes/manipulates objects that represent nodes
in a tree structure.  The tree structure is not an object itself, but
is emergent from the linkages you create between nodes.  This class
provides the methods for making linkages that can be used to build up
a tree, while preventing you from ever making any kinds of linkages
which are not allowed in a tree (such as having a node be its own
mother or ancestor, or having a node have two mothers).

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
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Tree/DAG_Node.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.05-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Initial package.
