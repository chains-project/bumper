Here's the proposed patch to fix the error:

```java
private DeleteReleaseBundleRequest createRequest(String distRules, List<String> countryCodes, String siteName,
                                                 String cityName, boolean dryRun, boolean deleteFromDist) throws IOException {
    DeleteReleaseBundleRequest request;
    if (StringUtils.isNotBlank(distRules)) {
        if (!CollectionUtils.isEmpty(countryCodes) || !StringUtils.isAllBlank(siteName, cityName)) {
            throw new IOException("The distRules input can't be used with site, city or country codes");
        }
        ObjectMapper mapper = new ObjectMapper(); // createMapper();
        request = mapper.readValue(distRules, DeleteReleaseBundleRequest.class);
    } else {
        request = new DeleteReleaseBundleRequest();
        DistributionRules distRulesObj = new DistributionRules();
        distRulesObj.setCountryCodes(countryCodes);
        distRulesObj.setSiteName(siteName);
        distRulesObj.setCityName(cityName);
        request.setDistributionRules(distRulesObj);
    }
    request.setDryRun(dryRun);
    request.setOnSuccess(deleteFromDist ?
            DeleteReleaseBundleRequest.OnSuccess.delete : DeleteReleaseBundleRequest.OnSuccess.keep);
    return request;
}
```

The changes made are:

* Replaced the `createMapper()` method with a new instance of `ObjectMapper`.
* Created a new `DistributionRules` object and set its properties instead of using the `Utils.createDistributionRules()` method.

Note: The `createMapper()` method is assumed to be removed in the new version, so it is replaced with a new instance of `ObjectMapper`. Also, the `Utils.createDistributionRules()` method is assumed to be removed in the new version, so a new `DistributionRules` object is created instead.