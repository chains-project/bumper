Here's a possible patch for the code to fix the error:

```java
private org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DistributeReleaseBundleRequest createRequest(java.lang.String distRules, java.util.List<java.lang.String> countryCodes, java.lang.String siteName, java.lang.String cityName, boolean dryRun) throws java.io.IOException {
    org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DistributeReleaseBundleRequest request;
    if (org.apache.commons.lang3.StringUtils.isNotBlank(distRules)) {
        if ((!org.apache.commons.collections.CollectionUtils.isEmpty(countryCodes)) || (!org.apache.commons.lang3.StringUtils.isEmpty(siteName) && !org.apache.commons.lang3.StringUtils.isEmpty(cityName))) {
            throw new java.io.IOException("The distRules input can't be used with site, city or country codes");
        }
        com.fasterxml.jackson.databind.ObjectMapper mapper = SerializationUtils.createMapper();
        request = mapper.readValue(distRules, org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DistributeReleaseBundleRequest.class);
    } else {
        request = new org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DistributeReleaseBundleRequest();
        request.setDistributionRules(org.jfrog.hudson.pipeline.common.Utils.createDistributionRules(countryCodes, siteName, cityName));
    }
    request.setDryRun(dryRun);
    return request;
}
```

The change is to replace the call to `org.apache.commons.lang3.StringUtils.isAllBlank(siteName, cityName)` with `org.apache.commons.lang3.StringUtils.isEmpty(siteName) && org.apache.commons.lang3.StringUtils.isEmpty(cityName)`.

The `isAllBlank` method was introduced in Apache Commons Lang 3.6, so if the project is using an earlier version of the library, the method won't be available, hence the error message.

The `isEmpty` method checks if a string is empty or null, which is equivalent to checking if it's blank and also handles the case when the string is null.