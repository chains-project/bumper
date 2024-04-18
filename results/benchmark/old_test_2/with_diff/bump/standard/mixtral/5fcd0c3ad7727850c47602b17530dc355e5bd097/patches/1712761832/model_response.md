Here's the fixed version of the `createSummaryData` method that should work with the updated library:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    org.pitest.classinfo.ClassInfoBuilder builder = org.pitest.classinfo.ClassInfo.builder();
    coverage.getRawCoverage(data.getMutatedClass()).ifPresent(rawCoverage -> {
        byte[] rawData = rawCoverage.getRawData();
        long timestamp = rawCoverage.getTimestamp();
        builder = builder.addRawData(data.getMutatedClass().asString(), rawData, timestamp);
    });
    org.pitest.classinfo.ClassInfo classInfo = builder.build();
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```

The main change is that we now manually build the `ClassInfo` object using the `ClassInfo.builder()` method, and add the raw coverage data to it. This is necessary because the `getClassInfo()` method has been removed from the `CoverageDatabase` class.

Note that this assumes that the `getRawCoverage()` method still exists and returns the same type of object as before. If that's not the case, you may need to adjust the code accordingly.