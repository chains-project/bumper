Here is a suggested patch for the given code:
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
The changes made include:

* Replacing the call to `createMapper()` with a new instantiation of `ObjectMapper`. This assumes that the `createMapper()` method no longer exists or is not available in the new version of the external dependency.
* Creating a new `DistributionRules` object in the case where `distRules` is `null` or empty. This object is then populated with the `countryCodes`, `siteName`, and `cityName` parameters. This assumes that the `createDistributionRules()` method is no longer available in the new version of the external dependency.

Note that these changes are based on assumptions about the changes in the external dependency. It's possible that the actual fix may require different changes.