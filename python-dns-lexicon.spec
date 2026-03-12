Name:		python-dns-lexicon
Version:	3.23.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/d/dns_lexicon/dns_lexicon-%{version}.tar.gz
Summary:	Manipulate DNS records on various DNS providers in a standardized/agnostic way
URL:		https://pypi.org/project/dns-lexicon/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Manipulate DNS records on various DNS providers in a standardized/agnostic way

%files
%{_bindir}/lexicon
%{py_sitedir}/lexicon
%{py_sitedir}/dns_lexicon-*.*-info
