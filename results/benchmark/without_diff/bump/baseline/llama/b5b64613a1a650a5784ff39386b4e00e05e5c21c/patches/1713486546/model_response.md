```
  private DistributeReleaseBundleRequest createRequest(String distRules, List<String> countryCodes,
                                                         String siteName, String cityName, boolean dryRun) throws IOException {
        DistributeReleaseBundleRequest request;
        if (StringUtils.isNotBlank(distRules)) {
            if (!CollectionUtils.isEmpty(countryCodes) || !StringUtils.isAllBlank(siteName, cityName)) {
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

Change `Utils.createDistributionRules(countryCodes, siteName, cityName)` to `DistributionRules.create(countryCodes, siteName, cityName)`.


The error message indicates that the `Utils` class cannot be found, which suggests that the `Utils` class is not in the project's classpath. To fix this issue, you can replace the `Utils.createDistributionRules()` method call with the `DistributionRules.create()` method call.


The `DistributionRules.create()` method is a static method that takes three parameters: `countryCodes`, `siteName`, and `cityName`. It returns a `DistributionRules` object that represents the distribution rules for the given inputs.


By replacing the `Utils.createDistributionRules()` method call with `DistributionRules.create()`, you are using a different method that is not dependent on the `Utils` class. This should fix the error and allow the code to compile successfully.