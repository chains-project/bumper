Here's the proposed patch for the client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, coverage.getRawCoverage(className), coverage.getTimestamp(className));
}
```

This patch introduces a new helper method `getClassInfoFromCoverage` which uses the new method `getClassInfo` from `org.pitest.classinfo.ClassInfoVisitor`. This method takes the class name, raw coverage, and timestamp to create a `ClassInfo` instance.

The `createSummaryData` method now uses the new helper method to retrieve the `ClassInfo` instead of relying on the deprecated method from `CoverageDatabase`.