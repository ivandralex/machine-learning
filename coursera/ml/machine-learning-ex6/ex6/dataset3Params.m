function [C, sigma] = dataset3Params(X, y, Xval, yval)
%EX6PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = EX6PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

values = [0.01 0.03 0.1 0.3 1 3 10 30]';

num_values = size(values, 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%

x1 = x2 = zeros(size(X(1)));

min_error = 1;

for i=1:num_values
	for j=1:num_values
		C = values(i);
		sigma = values(j);

		model= svmTrain(X, y, C, @(x1, x2) gaussianKernel(x1, x2, sigma));

		predictions = svmPredict(model, Xval);

		current_error = mean(double(predictions ~= yval));

		if current_error < min_error
			best_sigma = sigma;
			best_c = C;
			min_error = current_error;
		end
	end
end


C = best_c;
sigma = best_sigma;

% =========================================================================

end
