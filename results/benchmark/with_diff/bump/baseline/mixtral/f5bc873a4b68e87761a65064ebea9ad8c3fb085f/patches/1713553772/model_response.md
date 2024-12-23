Here's the fixed `unpackTheme` method with the required import statement:

```java
import org.eclipse.aether.resolution.ArtifactResolutionException;

@Override
public void unpackTheme(Theme theme) throws MojoExecutionException {
    try {
        Path targetDir = Paths.get(getOutputDirectory(), theme.getArtifactId());
        Files.createDirectories(targetDir);

        Artifact artifact = getArtifact(theme);
        ArtifactRequest request = new ArtifactRequest();
        request.setArtifact(artifact);
        request.setRepositorySystemSession(getRepositorySystemSession());
        ArtifactResult result = getRepositorySystem().resolveArtifact(request);
        File artifactFile = result.getArtifact().getFile();

        try (JarFile jarFile = new JarFile(artifactFile)) {
            Enumeration<? extends JarEntry> entries = jarFile.entries();
            while (entries.hasMoreElements()) {
                JarEntry entry = entries.nextElement();
                if (!entry.isDirectory()) {
                    String name = entry.getName();
                    if (name.startsWith("META-INF/resources/") && name.endsWith(".css")
                            || name.startsWith("META-INF/resources/") && name.endsWith(".js")) {
                        try (InputStream in = jarFile.getInputStream(entry);
                             OutputStream out = Files.newOutputStream(targetDir.resolve(name))) {

                            IOUtils.copy(in, out);
                        }
                    }
                }
            }
        }
    } catch (ArtifactResolutionException | IOException e) {
        throw new MojoExecutionException("Failed to unpack theme: " + theme.getArtifactId(), e);
    }
}
```

The `DependencyResolutionRequiredException` has been replaced with `ArtifactResolutionException` from the `org.eclipse.aether.resolution` package.