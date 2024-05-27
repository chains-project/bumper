Here's a fixed version of the `createRequest` method with the syntax error corrected:

```java
private org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DistributeReleaseBundleRequest createRequest(java.lang.String distRules, java.util.List<java.lang.String> countryCodes, java.lang.String siteName, java.lang.String cityName, boolean dryRun) throws java.io.IOException {
    org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DistributeReleaseBundleRequest request;
    if (org.apache.commons.lang3.StringUtils.isNotBlank(distRules)) {
        if ((!org.apache.commons.collections.CollectionUtils.isEmpty(countryCodes)) || ((!org.apache.commons.lang3.StringUtils.isBlank(org.apache.commons.lang3.StringUtils.defaultIfBlank(siteName, "").trim())) || (!org.apache.commons.lang3.StringUtils.isBlank(org.apache.commons.lang3.StringUtils.defaultIfBlank(cityName, "").trim())))) {
            throw new java.io.IOException("The distRules input can't be used with site, city or country codes");
        }
        com.fasterxml.jackson.databind.ObjectMapper mapper = org.jfrog.hudson.pipeline.common.executors.SerializationUtils.createMapper();
        request = mapper.readValue(distRules, org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DistributeReleaseBundleRequest.class);
    } else {
        request = new org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DistributeReleaseBundleRequest();
        request.setDistributionRules(org.jfrog.hudson.pipeline.common.Utils.createDistributionRules(countryCodes, siteName, cityName));
    }
    request.setDryRun(dryRun);
    return request;
}
```

The issue was caused by a missing closing parenthesis in the `if` statement. I have added the missing ')' to resolve the syntax error.