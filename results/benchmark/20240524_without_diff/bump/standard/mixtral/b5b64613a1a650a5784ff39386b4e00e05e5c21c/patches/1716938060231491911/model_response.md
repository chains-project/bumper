Here is the proposed patch for the failing client code:

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

private boolean isAllBlank(String siteName, String cityName) {
    return org.apache.commons.lang3.StringUtils.isBlank(siteName) && org.apache.commons.lang3.StringUtils.isBlank(cityName);
}
```

The proposed patch adds a new private method `isAllBlank` that checks if both `siteName` and `cityName` are blank. This method uses the `isBlank` method from `org.apache.commons.lang3.StringUtils` to check if a string is blank. The original `isAllBlank` method from `org.apache.commons.lang3.StringUtils` takes a variable number of arguments, but the updated method takes only two arguments, `siteName` and `cityName`.

The original code calls `isAllBlank` method with two arguments `siteName` and `cityName`, but the error message suggests that the method `isAllBlank` with two arguments is not found in `org.apache.commons.lang3.StringUtils`. Therefore, the proposed patch adds a new private method `isAllBlank` that checks if both `siteName` and `cityName` are blank. This way, the code can still achieve the same functionality, but without relying on the missing method from `org.apache.commons.lang3.StringUtils`.