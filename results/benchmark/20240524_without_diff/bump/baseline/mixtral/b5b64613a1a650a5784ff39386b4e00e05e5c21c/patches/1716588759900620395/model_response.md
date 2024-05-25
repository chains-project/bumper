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
        DistributionRules distRulesObj = Utils.createDistributionRules(countryCodes, siteName, cityName);
        if (distRulesObj != null) {
            request.setDistributionRules(distRulesObj);
        }
    }
    request.setDryRun(dryRun);
    request.setOnSuccess(deleteFromDist ?
            DeleteReleaseBundleRequest.OnSuccess.delete : DeleteReleaseBundleRequest.OnSuccess.keep);
    return request;
}
```

Changes made:

1. Replaced the `createMapper()` method with `new ObjectMapper()`.
2. Created a new variable `distRulesObj` for the result of `Utils.createDistributionRules()` and checked if it's not null before setting it to `request.setDistributionRules()`.

Note: I'm assuming `createMapper()` was causing the issue and it was a method for creating an instance of `ObjectMapper`. If that's not the case, you might need to adjust the code accordingly.