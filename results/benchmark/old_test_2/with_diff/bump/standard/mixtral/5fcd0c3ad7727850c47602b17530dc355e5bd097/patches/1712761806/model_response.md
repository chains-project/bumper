Here is a possible patch for the code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, coverage.getRawCoverage(className), coverage.getTimestamp());
}
```

The patch introduces a new helper method `getClassInfoFromCoverage` that uses the new method `getClassInfo` from `ClassInfoVisitor` to build a `ClassInfo` object from the coverage data. The `getClassInfo` method takes a `ClassName`, a byte array, and a long as arguments. The byte array and long are obtained from the `CoverageDatabase` by calling the `getRawCoverage` and `getTimestamp` methods, respectively. The `getClassInfo` method returns a `ClassInfoBuilder` object, which is then used to build the final `ClassInfo` object. The `getClassInfoFromCoverage` method is then called from the `createSummaryData` method instead of calling `getClassInfo` directly on the `CoverageDatabase` object.