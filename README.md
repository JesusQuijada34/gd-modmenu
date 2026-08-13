# GDH Geometry Dash Mod Menu

**Identidad del paquete:** `influent.gd-modmenu.v5.0-26.08-21.56`
**Autor:** `JesusQuijada34`
**Plataforma:** `AlphaCube`
**Descripción:** Estructura reparada por MoonFix

## Estructura PackageMaker 3.2.7

Este repositorio fue normalizado mediante **MoonFix**, usando la estructura de PackageMaker 3.2.7. El paquete público debe conservar `details.xml`, `version.res`, `autorun`, `autorun.bat`, `.storedetail`, `updater.py`, `config/settings.json`, los marcadores `.container` y los archivos de documentación correspondientes. El publisher oficial es `influent` y la versión pública no contiene sufijo de plataforma.

## Instalación y ejecución

Instala las dependencias declaradas en `lib/requirements.txt` cuando exista y ejecuta el entrypoint real del proyecto. En Linux, los comandos privilegiados son específicos de Danenone y no deben trasladarse a Windows. En proyectos AlphaCube, la validación Windows debe realizarse con el `buildthis` oficial de PackageMaker.

## Validación

La fuente debe pasar compilación sintáctica, pruebas funcionales disponibles, comprobación de identidad XML, protección contra traversal en ZIP y llamadas seguras a subprocess. Los artefactos `.iflapp` deben ser generados por PackageMaker; los paquetes Debian deben usar el nombre canónico `influent.gd-modmenu.v5.0-26.08-21.56_ARCH.deb`.

## Release

El tag y el título del release deben ser exactamente `v5.0-26.08-21.56`. Los assets deben usar el nombre canónico del paquete y una extensión objetiva. No se permite publicar un release AlphaCube que contenga únicamente el build Linux.

## Referencia original

<p align=center>
  <img src="logo.png" alt="GDH Logo" width=200 />
</p>

# GDH

GDH is an open-source Geometry Dash mod menu that aims to improve the game's performance and add new features.

## PackageMaker classification

This repository is distributed as **AlphaCube** source code. It is not a generic Linux or Windows binary: it requires the **Geode SDK**, Geometry Dash bindings, platform-specific build tooling, and the appropriate FFmpeg libraries for some targets. Build it through the included CMake configuration or the upstream Geode workflow; do not install a prebuilt `.iflapp` as if it were a standalone desktop application.

The replay subsystem validates macro names before constructing paths and checks output-file creation. Names containing path separators, traversal components, unsupported characters, or more than 128 characters are rejected. The static security check can be run with `python3 static_security_check.py`.

Это README также [доступно на русском языке](README.ru.md)

## Gallery
<img src="https://github.com/user-attachments/assets/b82e1a3d-b770-4830-bdce-2ef7a645d0e1" alt="Screenshot" width=800 />

## Install GDH directly through the mod catalogue in Geode itself (Recommended)
1. Make sure [Geode](https://geode-sdk.org/) is installed
2. In the mod install menu, under the Discover page, find GDH and install it
3. Restart the game
4. Press <kbd>Tab</kbd> to show the integrated menu

## Install GDH using Installer
[Complete Guide](https://github.com/TobyAdd/GDH-Installer/blob/main/README.md#how-to-install)

## Install GDH manually
1. Make sure [Geode](https://geode-sdk.org/) is installed
2. Download [tobyadd.gdh.geode](https://github.com/TobyAdd/GDH/releases/latest/download/tobyadd.gdh.geode)
3. Move it to `geode/mods/` folder in Geometry Dash directory (Library → GD → Right click → Browse local files)
4. Run GD and press <kbd>Tab</kbd> to show the integrated menu

## Pull requests and Issues
Feel free to submit a pull request.
Also, please, do not create silly issues like "how to install", "there is a virus/cryptominer" or any kind of suggestion.
If you want to propose an idea, you can do so on our [Discord server](https://discord.gg/ahYEz4MAwP).

---

Thanks to the [aciddev_](https://github.com/thisisignitedoreo) for the icon, small README improvements & translating it.<br/>
Thanks to all the [contributors](https://github.com/TobyAdd/GDH/graphs/contributors).
