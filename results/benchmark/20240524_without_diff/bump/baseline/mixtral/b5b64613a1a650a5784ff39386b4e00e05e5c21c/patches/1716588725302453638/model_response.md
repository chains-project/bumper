Here is a possible patch for the failing client code:

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

I made the following changes:

* Replaced the call to `createMapper()` with a new `ObjectMapper` instance. It's possible that the `createMapper()` method was removed or modified in the updated dependency.
* Replaced the call to `Utils.createDistributionRules()` with a new `DistributionRules` object. I assumed that `DistributionRules` is a class that can be instantiated and set the `countryCodes`, `siteName`, and `cityName` properties directly.

Note: These changes are based on assumptions about the missing or modified methods and classes. You may need to adjust the code based on the actual changes in the updated dependency.