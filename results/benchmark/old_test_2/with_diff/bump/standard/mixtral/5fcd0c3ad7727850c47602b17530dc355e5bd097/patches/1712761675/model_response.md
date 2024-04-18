Here is a possible patch for the failing method:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    byte[] bytes = coverage.getClassData(data.getMutatedClass()).getBytes();
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), org.pitest.classinfo.ClassInfoVisitor.getClassInfo(data.getMutatedClass(), bytes, coverage.getClassData(data.getMutatedClass()).getLineCount()));
}
```

This patch uses the new `getClassInfo` method added in the updated library version to get the `ClassInfo` for the mutated class, instead of the removed `getClassInfo` method from the `CoverageDatabase` class. It first gets the class data for the mutated class from the `CoverageDatabase`, then gets its bytes and line count, and finally uses them to create a `ClassInfo` object using the new `getClassInfo` method.