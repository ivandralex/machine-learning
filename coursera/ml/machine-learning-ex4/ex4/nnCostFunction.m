function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0; 
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%

% Theta1: 25 x 401
% Theta2: 10 x 26
% X: 5000 x 400
% y: 5000 x 1
% hidden_layer_size: 25
% num_labels: 10
% input_layer_size: 400

% Vectors of errors
delta_3 = zeros(num_labels, 1);
delta_2 = zeros(hidden_layer_size + 1, 1);

% X1: 5000 x 401
X1 = [ones(m, 1) X];
A2 = X1*Theta1';
% X2: 5000 x 26
X2 = sigmoid(A2);
X2 = [ones(m, 1) X2];
A2 = [ones(m, 1) A2];
% X3: 5000 x 10
h = sigmoid(X2*Theta2');
% Recoding (y(i) equals to the number of output)
Y = zeros(m, num_labels);

for i = 1:m
	for k = 1:num_labels
		Y(i, y(i)) = 1;

		J += 1/m * ( -Y(i, k)' * log(h(i, k)) - (1 - Y(i, k))' * log (1-h(i, k)) );
	end

	% delta_3: 10 x 1
	delta_3 = (h(i, :) - Y(i, :))';
	delta_2 = (Theta2' * delta_3) .* ((X2(i, :) .* (1 - X2(i, :)))');
	% delta_2: 25 x 1
	delta_2 = delta_2(2:end);
    
	Theta1_grad = Theta1_grad + delta_2*X1(i, :);
	Theta2_grad = Theta2_grad + delta_3*X2(i, :);
end

reg1 = lambda/m * Theta1;
reg1(:, 1) = 0;

reg2 = lambda/m * Theta2;
reg2(:, 1) = 0;

Theta1_grad = Theta1_grad ./ m + reg1;
Theta2_grad = Theta2_grad ./ m + reg2;

% Adding regularization terms

for j = 1:hidden_layer_size
	for k = 1:input_layer_size
		J += lambda/2/m * Theta1(j, k+1)^2;
	end
end

for j = 1:num_labels
	for k = 1:hidden_layer_size
		J += lambda/2/m * Theta2(j, k+1)^2;
	end
end

% Unregularized


%grad = 1 / m * X' * (h - y);

%theta1 = theta;
%theta1(1) = 0;

% Adding regularization terms
%J = J + lambda / 2 / m * theta1' * theta1;
%grad = grad + lambda / m * theta1;

% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end