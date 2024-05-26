Here is a possible patch for the failing client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, coverage.getRawCoverageData(className), coverage.getTimestamp(className));
}
```

Explanation:

The error message indicates that the method `getClassInfo(java.util.Collection)` is no longer available in the `CoverageDatabase` class. Instead, we can use the new method `getRawCoverageData(className)` to get the raw coverage data for a specific class, and then use the new static method `getClassInfo(className, byte[], long)` in the `ClassInfoVisitor` class to create a `ClassInfo` object from the raw data.

Therefore, I added a new helper method `getClassInfoFromCoverage(CoverageDatabase coverage, ClassName className)` that takes a `CoverageDatabase` object and a `ClassName` object, and returns a `ClassInfo` object. This method first retrieves the raw coverage data for the given class using the `getRawCoverageData(className)` method, and then creates a `ClassInfo` object using the `getClassInfo(className, byte[], long)` method.

In the `createSummaryData` method, I replaced the call to `coverage.getClassInfo(java.util.Collections.singleton(data.getMutatedClass()))` with a call to `getClassInfoFromCoverage(coverage, data.getMutatedClass())` to use the new helper method.