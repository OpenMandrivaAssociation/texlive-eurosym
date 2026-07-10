%global tl_name eurosym
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4~subrfix
Release:	%{tl_revision}.1
Summary:	Metafont and macros for Euro sign
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/eurosym
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eurosym.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eurosym.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The European currency symbol for the Euro implemented in Metafont, using
the official European Commission dimensions, and providing several
shapes (normal, slanted, bold, outline). The package also includes a
LaTeX package which defines the macro, pre-compiled tfm files, and
documentation.

