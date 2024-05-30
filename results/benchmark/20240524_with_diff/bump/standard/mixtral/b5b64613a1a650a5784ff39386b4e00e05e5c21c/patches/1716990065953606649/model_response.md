Here's the patched version of the `execute` method that fixes the error:
```java
public void execute() throws java.lang.Exception {
    if (server == null) {
        throw new java.lang.IllegalStateException("Artifactory server must be configured");
    }
    if (org.apache.commons.lang.StringUtils.isBlank(kanikoImageFile) && org.apache.commons.lang.StringUtils.isBlank(jibImageFile) || !org.apache.commons.lang.StringUtils.isBlank(kanikoImageFile) && !org.apache.commons.lang.StringUtils.isBlank(jibImageFile)) {
        throw new java.lang.IllegalStateException("Exactly one of 'kanikoImageFile' or 'jibImageFile' must be configured");
    }
    org.jfrog.hudson.pipeline.common.types.deployers.CommonDeployer deployer = new org.jfrog.hudson.pipeline.common.types.deployers.CommonDeployer();
    deployer.setServer(server);
    deployer.setRepo(sourceRepo);
    hudson.FilePath tempDir = org.jfrog.hudson.util.ExtractorUtils.createAndGetTempDir(ws);
    org.jfrog.hudson.pipeline.common.executors.EnvExtractor envExtractor = new org.jfrog.hudson.pipeline.common.executors.CreateDockerBuildEnvExtractor(build, buildInfo, deployer, listener, launcher, tempDir, env, kanikoImageFile, jibImageFile);
    super.execute("Create Docker Build", "org.jfrog.build.extractor.docker.extractor.BuildDockerCreator", envExtractor, tempDir);
}
```
The changes made are:

* Replace `isAllBlank` with `isBlank` to check if a string is empty or whitespace.
* Replace `isNoneBlank` with a combination of `isBlank` to check if exactly one of the two strings is non-empty.

This should resolve the compilation error and the code should work as intended.