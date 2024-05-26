Here's the updated `createSummaryData` method that should fix the error:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName className) {
    byte[] classBytes = coverage.getClassBytes(className);
    long timestamp = coverage.getTimestamp(className);
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, classBytes, timestamp);
}
```

This new implementation extracts the class info by using the new `getClassInfo` method from `ClassInfoVisitor`. It first retrieves the class bytes and timestamp from the `CoverageDatabase`, and then passes them to the `getClassInfo` method.