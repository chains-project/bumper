```java
private DeleteReleaseBundleRequest createRequest(String distRules, List<String> countryCodes, String siteName,
                                                     String cityName, boolean dryRun, boolean deleteFromDist) throws IOException {
        DeleteReleaseBundleRequest request;
        if (StringUtils.isNotBlank(distRules)) {
            if (!CollectionUtils.isEmpty(countryCodes) || !StringUtils.isAllBlank(siteName, cityName)) {
                throw new IOException("The distRules input can't be used with site, city or country codes");
            }
            ObjectMapper mapper = createMapper();
            request = mapper.readValue(distRules, DeleteReleaseBundleRequest.class);
        } else {
            request = new DeleteReleaseBundleRequest();
            request.setDistributionRules(Utils.createDistributionRules(countryCodes, siteName, cityName));
        }
        request.setDryRun(dryRun);
        DeleteReleaseBundleRequest.OnSuccess onSuccess = deleteFromDist ?
                DeleteReleaseBundleRequest.OnSuccess.delete : DeleteReleaseBundleRequest.OnSuccess.keep;
        request.setOnSuccess(onSuccess);
        return request;
    }
```