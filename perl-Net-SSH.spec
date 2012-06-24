#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	SSH
Summary:	Net::SSH Perl module
Summary(cs):	Modul Net::SSH pro Perl
Summary(da):	Perlmodul Net::SSH
Summary(de):	Net::SSH Perl Modul
Summary(es):	M�dulo de Perl Net::SSH
Summary(fr):	Module Perl Net::SSH
Summary(it):	Modulo di Perl Net::SSH
Summary(ja):	Net::SSH Perl �⥸�塼��
Summary(ko):	Net::SSH �� ����
Summary(nb):	Perlmodul Net::SSH
Summary(pl):	Modu� Perla Net::SSH
Summary(pt):	M�dulo de Perl Net::SSH
Summary(pt_BR):	M�dulo Perl Net::SSH
Summary(ru):	������ ��� Perl Net::SSH
Summary(sv):	Net::SSH Perlmodul
Summary(uk):	������ ��� Perl Net::SSH
Summary(zh_CN):	Net::SSH Perl ģ��
Name:		perl-Net-SSH
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c25a38f0b1d1b126cfb5dc231ac269da
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::SSH - perl wrapper for system 'ssh' command

%description -l pl
Net::SSH - interfejs do systemowego polecenia 'ssh'

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Net/SSH.pm
%{_mandir}/man3/*
