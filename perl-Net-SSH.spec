#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	SSH
Summary:	Net::SSH Perl module
Summary(cs):	Modul Net::SSH pro Perl
Summary(da):	Perlmodul Net::SSH
Summary(de):	Net::SSH Perl Modul
Summary(es):	Módulo de Perl Net::SSH
Summary(fr):	Module Perl Net::SSH
Summary(it):	Modulo di Perl Net::SSH
Summary(ja):	Net::SSH Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Net::SSH ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Net::SSH
Summary(pl):	Modu³ Perla Net::SSH
Summary(pt):	Módulo de Perl Net::SSH
Summary(pt_BR):	Módulo Perl Net::SSH
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Net::SSH
Summary(sv):	Net::SSH Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Net::SSH
Summary(zh_CN):	Net::SSH Perl Ä£¿é
Name:		perl-Net-SSH
Version:	0.07
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
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
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Net/SSH.pm
%{_mandir}/man3/*
