```java
  private DeleteReleaseBundleRequest createRequest(String distRules, List<String> countryCodes, String siteName,
                                                     String cityName, boolean dryRun, boolean deleteFromDist) throws IOException {
        if (StringUtils.isNotBlank(distRules)) {
            if (!CollectionUtils.isEmpty(countryCodes) || !StringUtils.isAllBlank(siteName, cityName)) {
                throw new IOException("The distRules input can't be used with site, city or country codes");
            }
            ObjectMapper mapper = createMapper();
            return mapper.readValue(distRules, DeleteReleaseBundleRequest.class);
        } else {
            DeleteReleaseBundleRequest request = new DeleteReleaseBundleRequest();
            request.setDistributionRules(Utils.createDistributionRules(countryCodes, siteName, cityName));
            request.setDryRun(dryRun);
            request.setOnSuccess(deleteFromDist ?
                    DeleteReleaseBundleRequest.OnSuccess.delete : DeleteReleaseBundleRequest.OnSuccess.keep);
            return request;
        }
    }
```