Name:		texlive-widetable
Version:	53409
Release:	2
Summary:	An environment for typesetting tables of specified width
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/widetable
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/widetable.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/widetable.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/widetable.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a new environment that, unlike tabularX,
typesets a table of specified width by working on the inter-
column glue; the tabular cells will all be stretched (or
shrunk) according to need. The package will use the e-TeX
arithmetic extensions if they are available (they are, in most
modern distributions).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/widetable
%doc %{_texmfdistdir}/doc/latex/widetable
#- source
%doc %{_texmfdistdir}/source/latex/widetable

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
