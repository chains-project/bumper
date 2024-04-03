Based on the error message and the library changes, it seems that the `getClassInfo` method of `CoverageDatabase` is no longer available in the new library version. Instead, there is a new `getClassInfo` method in `ClassInfoBuilder` that can be used. Here's a proposed patch for the failing method:

```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfoBuilder builder = new ClassInfoBuilder(data.getMutatedClass().getName(), data.getMutations());
    coverage.getRawCoverage(data.getMutatedClass()).ifPresent(rawData -> {
      for (CoverageInfo cInfo : rawData.getSegments()) {
        builder.add(cInfo.getMethodIdentifiers(), cInfo.getCounts());
      }
    });
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), builder.build());
  }
```

In this patch, we use the new `getClassInfo` method by creating a `ClassInfoBuilder` object and then adding the necessary coverage information to it. We retrieve the raw coverage data for the mutated class using the `getRawCoverage` method of `CoverageDatabase`, and then iterate over the segments in the raw data to add the coverage information to the `ClassInfoBuilder` object. Finally, we build the `ClassInfo` object using the `build` method of `ClassInfoBuilder` and return the `MutationTestSummaryData` object as before.