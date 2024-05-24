Here's a fixed version of the `createRequest` method, using the `isAnyBlank` method from Apache Commons Lang 3 instead of the non-existing `isAllBlank` method:

```java
private DistributeReleaseBundleRequest createRequest(String distRules, List<String> countryCodes,
                                                     String siteName, String cityName, boolean dryRun) throws IOException {
    DistributeReleaseBundleRequest request;
    if (StringUtils.isNotBlank(distRules)) {
        if (!CollectionUtils.isEmpty(countryCodes) || !StringUtils.isAnyBlank(siteName, cityName)) {
            throw new IOException("The distRules input can't be used with site, city or country codes");
        }
        ObjectMapper mapper = createMapper();
        request = mapper.readValue(distRules, DistributeReleaseBundleRequest.class);
    } else {
        request = new DistributeReleaseBundleRequest();
        request.setDistributionRules(Utils.createDistributionRules(countryCodes, siteName, cityName));
    }
    request.setDryRun(dryRun);
    return request;
}
```
This version uses the `isAnyBlank` method from Apache Commons Lang 3 to check if either `siteName` or `cityName` are blank. This method returns true if any of the provided strings are blank, null, or an empty string.