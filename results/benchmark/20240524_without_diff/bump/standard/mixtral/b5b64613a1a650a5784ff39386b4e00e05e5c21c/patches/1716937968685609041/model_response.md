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

private boolean isAllBlank(String s1, String s2) {
    return (s1 == null || s1.isBlank()) && (s2 == null || s2.isBlank());
}
```

The patch adds a new method `isAllBlank` that checks if both `s1` and `s2` are blank. This method is used in the `createRequest` method instead of the non-existing `isAllBlank` method from `org.apache.commons.lang3.StringUtils`.

Note that `isBlank` is a method from `java.util.String`, which was added in Java 11. If you are using a version of Java prior to 11, you can replace `s1.isBlank()` with `s1.equals("")` and `s2.isBlank()` with `s2.equals("")`.