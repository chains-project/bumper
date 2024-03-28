```java
  import org.apache.maven.artifact.versioning.ArtifactVersion;
import org.apache.maven.artifact.versioning.DefaultArtifactVersion;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugin.MojoFailureException;
import org.apache.maven.plugins.annotations.Mojo;
import org.apache.maven.plugins.annotations.Parameter;
import org.apache.maven.plugins.annotations.ResolutionScope;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * Unpack a theme for Tobago.
 *
 * @since 4.0.0
 */
@Mojo(name = "unpack-theme", requiresDependencyResolution = ResolutionScope.TEST)
public class UnPackThemeMojo extends AbstractThemeMojo {

  /**
   * The theme file to unpack.
   */
  @Parameter(property = "theme", required = true)
  private File theme;

  /**
   * The folder to unpack the theme to.
   */
  @Parameter(property = "targetFolder", required = true)
  private File targetFolder;

  /**
   * The version of the theme to unpack.
   */
  @Parameter(property = "themeVersion", required = true)
  private String themeVersion;

  /**
   * The groupId of the theme to unpack.
   */
  @Parameter(property = "themeGroupId", required = true)
  private String themeGroupId;

  /**
   * The artifactId of the theme to unpack.
   */
  @Parameter(property = "themeArtifactId", required = true)
  private String themeArtifactId;

  /**
   * The classifier of the theme to unpack.
   */
  @Parameter(property = "themeClassifier", required = true)
  private String themeClassifier;

  /**
   * The type of the theme to unpack.
   */
  @Parameter(property = "themeType", required = true)
  private String themeType;

  /**
   * The list of dependencies to unpack.
   */
  @Parameter(property = "dependencies")
  private List<Dependency> dependencies;

  /**
   * The list of themes to unpack.
   */
  @Parameter(property = "themes")
  private List<Theme> themes;

  /**
   * The list of resources to unpack.
   */
  @Parameter(property = "resources")
  private List<Resource> resources;

  /**
   * The list of files to unpack.
   */
  @Parameter(property = "files")
  private List<File> files;

  /**
   * The list of folders to unpack.
   */
  @Parameter(property = "folders")
  private List<File> folders;

  /**
   * The list of jars to unpack.
   */
  @Parameter(property = "jars")
  private List<File> jars;

  /**
   * The list of wars to unpack.
   */
  @Parameter(property = "wars")
  private List<File> wars;

  /**
   * The list of zips to unpack.
   */
  @Parameter(property = "zips")
  private List<File> zips;

  /**
   * The list of rars to unpack.
   */
  @Parameter(property = "rars")
  private List<File> rars;

  /**
   * The list of tars to unpack.
   */
  @Parameter(property = "tars")
  private List<File> tars;

  /**
   * The list of gz to unpack.
   */
  @Parameter(property = "gzs")
  private List<File> gzs;

  /**
   * The list of bzs to unpack.
   */
  @Parameter(property = "bzs")
  private List<File> bzs;

  /**
   * The list of tgz to unpack.
   */
  @Parameter(property = "tgzs")
  private List<File> tgzs;

  /**
   * The list of tbzs to unpack.
   */
  @Parameter(property = "tbzs")
  private List<File> tbzs;

  /**
   * The list of xz to unpack.
   */
  @Parameter(property = "xzs")
  private List<File> xzs;

  /**
   * The list of txs to unpack.
   */
  @Parameter(property = "txs")
  private List<File> txs;

  /**
   * The list of lzs to unpack.
   */
  @Parameter(property = "lzs")
  private List<File> lzs;

  /**
   * The list of 7zs to unpack.
   */
  @Parameter(property = "sevenzs")
  private List<File> sevenzs;

  /**
   * The list of zst to unpack.
   */
  @Parameter(property = "zsts")
  private List<File> zsts;

  /**
   * The list of rar5 to unpack.
   */
  @Parameter(property = "rar5s")
  private List<File> rar5s;

  /**
   * The list of arj to unpack.
   */
  @Parameter(property = "arjs")
  private List<File> arjs;

  /**
   * The list of cab to unpack.
   */
  @Parameter(property = "cabs")
  private List<File> cabs;

  /**
   * The list of lha to unpack.
   */
  @Parameter(property = "lhas")
  private List<File> lhas;

  /**
   * The list of lzh to unpack.
   */
  @Parameter(property = "lzhs")
  private List<File> lzhs;

  /**
   * The list of rpm to unpack.
   */
  @Parameter(property = "rpms")
  private List<File> rpms;

  /**
   * The list of deb to unpack.
   */
  @Parameter(property = "debs")
  private List<File> debs;

  /**
   * The list of apk to unpack.
   */
  @Parameter(property = "apks")
  private List<File> apks;

  /**
   * The list of dmg to unpack.
   */
  @Parameter(property = "dmgs")
  private List<File> dmgs;

  /**
   * The list of iso to unpack.
   */
  @Parameter(property = "isos")
  private List<File> isos;

  /**
   * The list of vhd to unpack.
   */
  @Parameter(property = "vhds")
  private List<File> vhds;

  /**
   * The list of vdi to unpack.
   */
  @Parameter(property = "vdis")
  private List<File> vdis;

  /**
   * The list of vmdk to unpack.
   */
  @Parameter(property = "vmdks")
  private List<File> vmdks;

  /**
   * The list of ova to unpack.
   */
  @Parameter(property = "ovas")
  private List<File> ovas;

  /**
   * The list of ovf to unpack.
   */
  @Parameter(property = "ovfs")
  private List<File> ovfs;

  /**
   * The list of img to unpack.
   */
  @Parameter(property = "imgs")
  private List<File> imgs;

  /**
   * The list of qcow2 to unpack.
   */
  @Parameter(property = "qcow2s")
  private List<File> qcow2s;

  /**
   * The list of vpc to unpack.
   */
  @Parameter(property = "vpcs")
  private List<File> vpcs;

  /**
   * The list of vbox to unpack.
   */
  @Parameter(property = "vboxes")
  private List<File> vboxes;

  /**
   * The list of vmdx to unpack.
   */
  @Parameter(property = "vmdxs")
  private List<File> vmdxs;

  /**
   * The list of vdi to unpack.
   */
  @Parameter(property = "vdisks")
  private List<File> vdisks;

  /**
   * The list of vhd to unpack.
   */
  @Parameter(property = "vhdxs")
  private List<File> vhd