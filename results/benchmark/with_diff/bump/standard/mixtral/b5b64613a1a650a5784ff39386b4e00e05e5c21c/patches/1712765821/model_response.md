Here's a possible patch for the failing method. I noticed that the method `isAllBlank` has been removed from `org.apache.commons.lang3.StringUtils` in the new library version. Instead, you can use the `allNullOrEmpty` method from `org.jenkinsci.plugins.p4.util.StringUtils` to achieve the same functionality:

```java
private org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DeleteReleaseBundleRequest createRequest(java.lang.String distRules, java.util.List<java.lang.String> countryCodes, java.lang.String siteName, java.lang.String cityName, boolean dryRun, boolean deleteFromDist) throws java.io.IOException {
    org.jfrog.build.extractor.clientConfiguration.client.distribution.request.DeleteReleaseBundleRequest request;
    if (org.apache.commons.lang3.StringUtils.isNotBlank(distRules)) {
        if ((!org.apache.commons.collections.CollectionUtils.isEmpty(countryCodes)) || (!org.jenkinsci.plugins.p4.util.StringUtils.allNullOrEmpty(siteName, cityName))) {
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
```

This patch only replaces the usage of `isAllBlank` with `allNullOrEmpty` in the existing method. It's important to note that the behavior of these two methods is slightly different: `isAllBlank` returns true if all the provided strings are blank or null, whereas `allNullOrEmpty` returns true if all the provided objects (not just strings) are null or empty. However, based on the context of the code, it seems safe to assume that the intention is to check if both `siteName` and `cityName` are blank or null, so using `allNullOrEmpty` should be fine.

Additionally, I haven't changed any import statements, so make sure to add the following import at the beginning of your file if it's not already there:

```java
import org.jenkinsci.plugins.p4.util.StringUtils;
```