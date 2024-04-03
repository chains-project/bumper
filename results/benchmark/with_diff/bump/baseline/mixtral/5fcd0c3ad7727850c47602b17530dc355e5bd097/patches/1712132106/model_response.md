Based on the error message and the library changes, it seems that the `getClassInfo` method of `CoverageDatabase` is no longer available. Instead, a new `getClassInfo` method is added to `ClassInfoVisitor`. Here is a possible patch for the failing method:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfoVisitor visitor = new ClassInfoVisitor();
    coverage.getRawCoverageData().visit(visitor);
    Map<ClassName, Resource coverageData> coverageMap = visitor.getResult();
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(),
        coverageMap.get(data.getMutatedClass()).getFirstClassFileInfo());
}
```

In this patch, we use the `getRawCoverageData` method of `CoverageDatabase` to obtain the raw coverage data, and then visit it using a new `ClassInfoVisitor`. The `visit` method of `RawCoverageData` will call the `visit` method of `ClassInfoVisitor` for each class in the coverage data. We then extract the coverage data for the mutated class from the result of `ClassInfoVisitor`, and get the first class file info from it.

Note that this patch assumes that the coverage data for each class contains only one class file. If this is not the case, you may need to modify the patch accordingly.