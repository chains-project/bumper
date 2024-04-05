Here is a possible patch for the given code:
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
    return org.apache.commons.lang3.StringUtils.isAllBlank(siteName) && org.apache.commons.lang3.StringUtils.isAllBlank(cityName);
}
```
The patch introduces a new private method `isAllBlank` that checks if both `siteName` and `cityName` are blank. This method uses `org.apache.commons.lang3.StringUtils.isAllBlank` to check if a single string is blank.

The original code uses `org.apache.commons.lang3.StringUtils.isAllBlank` with two arguments, but this method does not exist. The new `isAllBlank` method takes two arguments and checks if both of them are blank using `org.apache.commons.lang3.StringUtils.isAllBlank` with a single argument.

The patch also removes the import statement for `org.apache.commons.lang3.StringUtils` and adds a new import statement for `org.jfrog.hudson.pipeline.common.Utils`. This is because the `createDistributionRules` method is used in the original code, which is located in the `Utils` class.

Note that the new `isAllBlank` method can be further optimized by using a single regular expression to check if both `siteName` and `cityName` are blank. However, this optimization is not necessary for the patch to work correctly.