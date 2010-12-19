# Generated from mixlib-authentication-1.1.4.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname mixlib-authentication
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Mixes in simple per-request authentication
Name: rubygem-%{gemname}
Version: 1.1.4
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://www.opscode.com
Source0: http://gemcutter.orggems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem(mixlib-log) >= 0
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Mixes in simple per-request authentication


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/NOTICE
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Sun Dec 19 2010 Sergio Rubio <rubiojr@frameos.org> - 1.1.4-1
- Initial package
