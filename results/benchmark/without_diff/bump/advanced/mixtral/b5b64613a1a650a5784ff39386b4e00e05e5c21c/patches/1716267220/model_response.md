Here is a possible patch for the code:

```java
private org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DeleteReleaseBundleRequest createRequest(java.lang.String distRules, java.util.List<java.lang.String> countryCodes, java.lang.String siteName, java.lang.String cityName, boolean dryRun, boolean deleteFromDist) throws java.io.IOException {
    org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DeleteReleaseBundleRequest request;
    if (org.apache.commons.lang3.StringUtils.isNotBlank(distRules)) {
        if ((!org.apache.commons.collections.CollectionUtils.isEmpty(countryCodes)) || (!isAllBlank(siteName, cityName))) {
            throw new java.io.IOException("The distRules input can't be used with site, city or country codes");
        }
        com.fasterxml.jackson.databind.ObjectMapper mapper = SerializationUtils.createMapper();
        request = mapper.readValue(distRules, org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DeleteReleaseBundleRequest.class);
    } else {
        request = new org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DeleteReleaseBundleRequest();
        request.setDistributionRules(org.jfrog.hudson.pipeline.common.Utils.createDistributionRules(countryCodes, siteName, cityName));
    }
    request.setDryRun(dryRun);
    request.setOnSuccess(deleteFromDist ? DeleteReleaseBundleRequest.OnSuccess.delete : DeleteReleaseBundleRequest.OnSuccess.keep);
    return request;
}

private boolean isAllBlank(String str1, String str2) {
    return (str1 == null || str1.isBlank()) && (str2 == null || str2.isBlank());
}
```

The patch adds a new method `isAllBlank` to the `ReleaseBundleDeleteExecutor` class, which checks if both `str1` and `str2` are blank or null. This method is used in the `createRequest` method instead of the `isAllBlank` method from `org.apache.commons.lang3.StringUtils`, which is causing the error.

The `isAllBlank` method uses the `isBlank` method from `java.util.String`, which is available since Java 11. If you are using an older version of Java, you can replace `str.isBlank()` with `str.isEmpty() || str.trim().isEmpty()`.

Note that the patch does not change the function signature or use any removed library methods. It only adds a new method to the class and uses it in the existing code.