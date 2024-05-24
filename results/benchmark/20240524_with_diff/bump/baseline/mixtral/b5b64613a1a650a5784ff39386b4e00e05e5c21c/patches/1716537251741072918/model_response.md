Here's the fixed `checkInputs` method with the necessary changes to use the new library version:

```java
private void checkInputs(JFrogPlatformInstance server) throws IOException {
    ClientHelper clientHelper = new ClientHelper(server, server.getTaskListener(), null, new Workspace());
    if (isAllBlank(server.getUrl(), getUrlFromClientHelper(clientHelper), server.getDistribution().getUrl(),
            step.url, step.artifactoryUrl, step.distributionUrl)) {
        throw new IOException("Server URL is missing");
    }
    if (isNotBlank(step.credentialsId)) {
        if (isNotBlank(step.username)) {
            throw new IOException("'rtServer' step can't include both credentialsId and username");
        }
        if (isNotBlank(step.password)) {
            throw new IOException("'rtServer' step can't include both credentialsId and password");
        }
    }
}

private String getUrlFromClientHelper(ClientHelper clientHelper) {
    return clientHelper.getChange(clientHelper.getClientHead()).getAction().getDepotPath();
}
```

The changes include:

1. Creating a new `ClientHelper` instance with the new constructor.
2. Adding a new helper method `getUrlFromClientHelper` to get the URL from the `ClientHelper`.
3. Updating the `isAllBlank` method call to include the new URL from the `ClientHelper`.

Note: I made assumptions about the library classes and methods based on the provided context. The solution might need adjustments depending on the actual library and its implementation details.