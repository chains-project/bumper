Here is a possible patch for the client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfoBuilder.from(className)
        .withCoverage(coverage.getRawHits(className), coverage.getRawCount(className))
        .build();
}
```

This patch introduces a new helper method `getClassInfoFromCoverage` that constructs a `ClassInfo` object from the `CoverageDatabase` using the new `ClassInfoBuilder` method. The original `createSummaryData` method is modified to use this helper method and pass the `MutatedClass` to it.

Note that this patch assumes that the `MutatedClass` returned by `data.getMutatedClass()` is an instance of `ClassName`. If this is not the case, the conversion from `MutatedClass` to `ClassName` needs to be added to the `getClassInfoFromCoverage` method.