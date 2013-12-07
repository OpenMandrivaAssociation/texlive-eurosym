# revision 17265
# category Package
# catalog-ctan /fonts/eurosym
# catalog-date 2009-03-31 14:27:12 +0200
# catalog-license other-free
# catalog-version 1.4-subrfix
Name:		texlive-eurosym
Version:	1.4
Release:	5
Summary:	MetaFont and macros for Euro sign
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/eurosym
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eurosym.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eurosym.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The new European currency symbol for the Euro implemented in
MetaFont, using the official European Commission dimensions,
and providing several shapes (normal, slanted, bold, outline).
The package also includes a LaTeX package which defines the
macro, pre-compiled tfm files, and documentation.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/eurosym/eurosym.map
%{_texmfdistdir}/fonts/source/public/eurosym/fey.mf
%{_texmfdistdir}/fonts/source/public/eurosym/feybl10.mf
%{_texmfdistdir}/fonts/source/public/eurosym/feybo10.mf
%{_texmfdistdir}/fonts/source/public/eurosym/feybr10.mf
%{_texmfdistdir}/fonts/source/public/eurosym/feyml10.mf
%{_texmfdistdir}/fonts/source/public/eurosym/feymo10.mf
%{_texmfdistdir}/fonts/source/public/eurosym/feymr10.mf
%{_texmfdistdir}/fonts/tfm/public/eurosym/feybl10.tfm
%{_texmfdistdir}/fonts/tfm/public/eurosym/feybo10.tfm
%{_texmfdistdir}/fonts/tfm/public/eurosym/feybr10.tfm
%{_texmfdistdir}/fonts/tfm/public/eurosym/feyml10.tfm
%{_texmfdistdir}/fonts/tfm/public/eurosym/feymo10.tfm
%{_texmfdistdir}/fonts/tfm/public/eurosym/feymr10.tfm
%{_texmfdistdir}/fonts/type1/public/eurosym/feybl10.pfb
%{_texmfdistdir}/fonts/type1/public/eurosym/feybo10.pfb
%{_texmfdistdir}/fonts/type1/public/eurosym/feybr10.pfb
%{_texmfdistdir}/fonts/type1/public/eurosym/feyml10.pfb
%{_texmfdistdir}/fonts/type1/public/eurosym/feymo10.pfb
%{_texmfdistdir}/fonts/type1/public/eurosym/feymr10.pfb
%{_texmfdistdir}/fonts/type1/public/eurosym/geybl10.pfb
%{_texmfdistdir}/fonts/type1/public/eurosym/geybo10.pfb
%{_texmfdistdir}/fonts/type1/public/eurosym/geybr10.pfb
%{_texmfdistdir}/fonts/type1/public/eurosym/geyml10.pfb
%{_texmfdistdir}/fonts/type1/public/eurosym/geymo10.pfb
%{_texmfdistdir}/fonts/type1/public/eurosym/geymr10.pfb
%{_texmfdistdir}/tex/latex/eurosym/eurosym.sty
%doc %{_texmfdistdir}/doc/fonts/eurosym/COPYING
%doc %{_texmfdistdir}/doc/fonts/eurosym/Changes
%doc %{_texmfdistdir}/doc/fonts/eurosym/Makefile
%doc %{_texmfdistdir}/doc/fonts/eurosym/README
%doc %{_texmfdistdir}/doc/fonts/eurosym/README.type1
%doc %{_texmfdistdir}/doc/fonts/eurosym/c/Makefile
%doc %{_texmfdistdir}/doc/fonts/eurosym/eurosym.cpp
%doc %{_texmfdistdir}/doc/fonts/eurosym/makemfs
%doc %{_texmfdistdir}/doc/fonts/eurosym/rundvips
%doc %{_texmfdistdir}/doc/fonts/eurosym/runlatex
%doc %{_texmfdistdir}/doc/fonts/eurosym/src/Makefile
%doc %{_texmfdistdir}/doc/fonts/eurosym/testeuro.pdf
%doc %{_texmfdistdir}/doc/fonts/eurosym/testeuro.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.4-2
+ Revision: 751667
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.4-1
+ Revision: 720562
- texlive-eurosym
- texlive-eurosym
- texlive-eurosym
- texlive-eurosym

