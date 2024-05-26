Here is a possible patch for the failing client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, coverage.getRawCoverage(className), coverage.getTimestamp());
}
```

Explanation:

The error message indicates that the method `getClassInfo` with a `Set<ClassName>` parameter has been removed from `CoverageDatabase`. Instead, the new library version provides a static method `getClassInfo` with a `ClassName`, `byte[]`, and `long` parameter in `ClassInfoVisitor`.

To fix the error, we can use the new method to get the `ClassInfo` for the given `ClassName`. We can extract a helper method `getClassInfoFromCoverage` to encapsulate the logic of getting the `ClassInfo` from `CoverageDatabase`.

Note that we need to convert the `MutatedClass` to `ClassName` before passing it to `getClassInfoFromCoverage`. We can assume that `MutatedClass` has a method `getClassName` that returns the corresponding `ClassName`.

The updated code uses the new method to get the `ClassInfo` and passes it to `MutationTestSummaryData`.

Note: This is just one possible solution. There might be other ways to fix the error depending on the specific requirements and constraints of the project.