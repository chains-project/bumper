```java
// TODO: review this AI generated patch!
private org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DeleteReleaseBundleRequest createRequest(java.lang.String distRules, java.util.List<java.lang.String> countryCodes, java.lang.String siteName, java.lang.String cityName, boolean dryRun, boolean deleteFromDist) throws java.io.IOException {
    org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DeleteReleaseBundleRequest request;
    if (org.apache.commons.lang3.StringUtils.isNotBlank(distRules)) {
        if (((!org.apache.commons.collections.CollectionUtils.isEmpty(countryCodes)) || (!org.apache.commons.lang3.StringUtils.isEmpty(siteName))) || (!org.apache.commons.lang3.StringUtils.isEmpty(cityName))) {
            throw new java.io.IOException("The distRules input can't be used with site, city or country codes");
        }
        com.fasterxml.jackson.databind.ObjectMapper mapper = org.jfrog.hudson.pipeline.common.executors.SerializationUtils.createMapper();
        request = mapper.readValue(distRules, org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DeleteReleaseBundleRequest.class);
    } else {
        request = new org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DeleteReleaseBundleRequest();
        if (!org.apache.commons.collections.CollectionUtils.isEmpty(countryCodes)) {
            request.setDistributionRules(org.jfrog.hudson.pipeline.common.Utils.createDistributionRules(countryCodes, null, null));
        } else if (!org.apache.commons.lang3.StringUtils.isEmpty(siteName)) {
            request.setDistributionRules(org.jfrog.hudson.pipeline.common.Utils.createDistributionRules(null, siteName, null));
        } else if (!org.apache.commons.lang3.StringUtils.isEmpty(cityName)) {
            request.setDistributionRules(org.jfrog.hudson.pipeline.common.Utils.createDistributionRules(null, null, cityName));
        }
    }
    request.setDryRun(dryRun);
    request.setOnSuccess(deleteFromDist ? DeleteReleaseBundleRequest.OnSuccess.delete : DeleteReleaseBundleRequest.OnSuccess.keep);
    return request;
}
```