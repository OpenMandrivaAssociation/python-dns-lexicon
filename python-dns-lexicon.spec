%define module dns-lexicon
%define oname dns_lexicon

Name:		python-dns-lexicon
Version:	3.24.0
Release:	1
Summary:	Manipulate DNS records on various DNS providers in a standardized/agnostic way
License:	None
Group:		Development/Python
URL:		https://pypi.org/project/dns-lexicon/
Source0:	https://files.pythonhosted.org/packages/source/d/%{oname}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(wheel)

%description
Manipulate DNS records on various DNS providers in a standardized/agnostic way

%files
%{_bindir}/lexicon
%{py_sitedir}/lexicon
%{py_sitedir}/%{oname}-%{version}.dist-info
